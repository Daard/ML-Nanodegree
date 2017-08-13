import hist
import cov
import mask
import csv_builder


# create models for images in directory dir
def build(dir):
    hist.build(dir)
    mask.build(dir)
    cov.build(dir)
    csv_builder.build(dir)