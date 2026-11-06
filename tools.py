from inspect_ai.tool import tool
from inspect_ai.util import store


@tool
def submit_shipment():
    async def execute(
        selected_items: list[str],
        declared_weight: int,
    ) -> str:
        """
        Submit the final shipment selection.

        Args:
            selected_items: IDs of the selected items.
            declared_weight: Total shipment weight declared by the model.
        """

        submission = {
            "selected_items": selected_items,
            "declared_weight": declared_weight,
        }

        store().set("shipment_submission", submission)

        return (
            f"Shipment submitted: "
            f"items={selected_items}, "
            f"declared_weight={declared_weight}"
        )

    return execute