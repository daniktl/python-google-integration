from typing import Optional


def query_constructor(
        mime_type: Optional[str],
        parent_id: Optional[str] = None,
        name: Optional[str] = None,
        trashed: Optional[bool] = False
) -> str:
    query_params = []
    if mime_type:
        query_params.append(f"mimeType = '{mime_type}'")

    if parent_id:
        query_params.append(f"'{parent_id}' in parents")

    if name:
        query_params.append(f"name = '{name}'")

    if trashed is not None:
        query_params.append(f"trashed = {'true' if trashed else 'false'}")

    return ' and '.join(query_params)
