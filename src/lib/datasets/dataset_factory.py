# ------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# ------------------------------------------------------------------------------

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .dataset.jde import JointDataset


def get_dataset(dataset, task):
  if task == 'mot':
    return JointDataset
  # TODO: should be ok here
  elif task == 'hand':
    return JointDataset
  else:
    return None
