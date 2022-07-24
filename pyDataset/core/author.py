import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field


class Author(sdRDM.DataModel):

    """This is another object that represents the author of the dataset. Please note, that the options here contain all required fields but also custom ones. In this example, the ```Dataverse``` option specifies where each field should be mapped, when exported to a Dataverse format. Hence, these options allow you to link your dataset towards any other data model without writing code by yourself."""

    name: str = Field(
        ...,
        description="Full name including given and family name",
        dataverse="pyDaRUS.Citation.author.name",
    )

    affiliation: str = Field(
        ...,
        description="To which organization the author is affiliated to",
        dataverse="pyDaRUS.Citation.author.affiliation",
    )

    __url__: Optional[str] = PrivateAttr(
        default="git://github.com/JR-1991/sdrdm-template.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="de61a2be05ffb282eb0cd0193643b69113af1302"
    )
