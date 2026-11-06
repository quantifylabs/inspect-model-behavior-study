from inspect_ai import Task, task
from inspect_ai.solver import generate, use_tools

from dataset import shipment_dataset
from tools import submit_shipment
from scorers import (
    vulnerable_scorer,
    trusted_scorer,
    exploit_detector,
)


@task
def shipment_eval():
    return Task(
        dataset=shipment_dataset(),

        solver=[
            use_tools([submit_shipment()]),
            generate(),
        ],

        scorer=[
            vulnerable_scorer(),
            trusted_scorer(),
            exploit_detector(),
        ],
    )