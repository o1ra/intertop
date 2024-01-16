from pathlib import Path
import intertop_tests


def to_resource(path: str):
    return (
        Path(intertop_tests.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
