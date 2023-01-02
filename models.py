"""This unit contains dataclasses serving as models to verify arguments"""
from dataclasses import dataclass, field
import marshmallow
# ---------------------------------------------------------------------------


@dataclass
class RequestArgs:
    """This class contains the arguments to verify"""
    cmd_1: str = field(metadata={'data_key': 'cmd1'})
    cmd_2: str = field(metadata={'data_key': 'cmd2'})
    value_1: str = field(metadata={'data_key': 'value1'})
    value_2: str = field(metadata={'data_key': 'value2'})
    file: str

    class Meta:
        """This class serves to ignore excessive arguments"""
        unknown = marshmallow.EXCLUDE
