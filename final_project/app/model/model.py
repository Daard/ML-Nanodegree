import hist
import cov
import mask
import csv_builder



def build(dir):
    hist.build(dir)
    mask.build(dir)
    cov.build(dir)
    csv_builder.build(dir)