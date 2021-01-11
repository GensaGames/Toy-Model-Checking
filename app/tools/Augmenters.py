from imgaug.augmenters import CoarseDropout, AllChannelsCLAHE, Fliplr, MultiplyAndAddToBrightness, Multiply
from imgaug.augmenters import Sequential
from imgaug.augmenters import Sometimes


# Also check with:
# AllChannelsHistogramEqualization()
def get_new_training():
    return Sequential([
        Multiply((1.0, 2.5), per_channel=0.5),
        Fliplr(0.5),
    ])


def get_new_validation():
    return Sequential([
        Multiply(1.8, per_channel=0.5),
    ])


def get_new_empty():
    return Sequential([
    ])
