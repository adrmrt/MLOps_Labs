from deepchecks.core import CheckResult, ConditionCategory, ConditionResult, DatasetKind
from deepchecks.vision import SingleDatasetCheck, VisionData
from deepchecks.vision.context import Context

from typing import Any


class FGSMAttackCheck(SingleDatasetCheck):
    """A check to test if the model is robust to FGSM attacks."""

    # TODO: Add epsilon as a parameter.
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # You can ignore the following method, we don't need it for this check, except to initialize the cache.
    def initialize_run(self, context: Context, dataset_kind: DatasetKind):
        # Initialize cache. You can use a different data structure if you want.
        self.cache = {}

    def update(self, context: Context, batch: Any, dataset_kind: DatasetKind):
        # TODO: The attack should go here. Use the samples in `batch` to create the adversarial samples.
        # and attack the model with the adversarial samples. Then, check how many of the adversarial samples
        # are misclassified by the model.
        # Cache the number of failing samples and the indices of the failing samples.
        batch_data_dict = ...

        # Add the results to the cache. You will need to change the line below.
        self.cache.update(batch_data_dict)

    def compute(self, context: Context, dataset_kind: DatasetKind) -> CheckResult:
        # Get the results from the cache and compute the ratio of failing samples.
        # Also report the indices of the failing samples.

        failing_samples = ...  # TODO: Get the failing samples from the cache.

        result = {
            "ratio": len(failing_samples) / len(self.cache),
            "indices": failing_samples.keys(),
        }

        # TODO: Create a matplotlib to display the ratio of failing samples.
        # (yes, you have my permission create a pie chart)

        # Pass the matplotlib figure to the display variable.
        display = None

        return CheckResult(result, display=display)
