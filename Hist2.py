#!/usr/bin/env python


import numpy # Hint to PyInstaller
import cv2
import scipy.io
import scipy.sparse

class HistogramClassifier(object):

    def __init__(self):

        self.verbose = False
        self.minimumSimilarityForPositiveLabel = 0.075

        self._channels = range(3)
        self._histSize = [256] * 3
        self._ranges = [0, 255] * 3
        self._references = {}

    def _createNormalizedHist(self, image, sparse):
        # Create the histogram.
        hist = cv2.calcHist([image], self._channels, None,
                            self._histSize, self._ranges)
        # Normalize the histogram.
        hist[:] = hist * (1.0 / numpy.sum(hist))
        # Convert the histogram to one column for efficient storage.
        hist = hist.reshape(16777216, 1)  # 16777216 == pow(2, 24)
        if sparse:
            # Convert the histogram to a sparse matrix.
            hist = scipy.sparse.csc_matrix(hist)
        return hist

    def addReference(self, image, label):
        hist = self._createNormalizedHist(image, True)
        if label not in self._references:
            self._references[label] = [hist]
        else:
            self._references[label] += [hist]

    def addReferenceFromFile(self, path, label):
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        self.addReference(image, label)

    def classify(self, queryImage, queryImageName=None):
        queryHist = self._createNormalizedHist(queryImage, False)
        bestLabel = 'Unknown'
        bestSimilarity = self.minimumSimilarityForPositiveLabel
        if self.verbose:
            print('================================================')
            if queryImageName is not None:
                print('Query image:')
                print('    %s' % queryImageName)
            print('Mean similarity to reference images by label:')
        for label, referenceHists in self._references.items():
            similarity = 0.0
            for referenceHist in referenceHists:
                similarity += cv2.compareHist(
                        referenceHist.todense(), queryHist,
                        cv2.HISTCMP_INTERSECT)
            similarity /= len(referenceHists)
            if self.verbose:
                print('    %8f  %s' % (similarity, label))
            if similarity > bestSimilarity:
                bestLabel = label
                bestSimilarity = similarity
        if self.verbose:
            print('================================================')
        return bestLabel

    def classifyFromFile(self, path, queryImageName=None):
        if queryImageName is None:
            queryImageName = path
        queryImage = cv2.imread(path, cv2.IMREAD_COLOR)
        return self.classify(queryImage, queryImageName)

    def serialize(self, path, compressed=False):
        file = open(path, 'wb')
        scipy.io.savemat(
            file, self._references, do_compression=compressed)

    def deserialize(self, path):
        file = open(path, 'rb')
        self._references = scipy.io.loadmat(file)
        for key in list(self._references.keys()):
            value = self._references[key]
            if not isinstance(value, numpy.ndarray):
                # This entry is serialization metadata so delete it.
                del self._references[key]
                continue
            # The serializer wraps the data in an extra array.
            # Unwrap the data.
            self._references[key] = value[0]

def main():
    classifier = HistogramClassifier()
    classifier.verbose = True
    classifier.addReferenceFromFile(r'D:\0.jpg','Stalinist, interior')
    classifier.serialize('classifier.mat')
    classifier.deserialize('classifier.mat')
    classifier.classifyFromFile(r'D:\1.jpg')

if __name__ == '__main__':
    main()