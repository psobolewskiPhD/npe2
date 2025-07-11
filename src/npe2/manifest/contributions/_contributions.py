from typing import Dict, List, Optional

from npe2._pydantic_compat import BaseModel, Field, validator

from ._commands import CommandContribution
from ._configuration import ConfigurationContribution
from ._keybindings import KeyBindingContribution
from ._menus import MenuItem
from ._readers import ReaderContribution
from ._sample_data import SampleDataContribution, SampleDataGenerator, SampleDataURI
from ._submenu import SubmenuContribution
from ._themes import ThemeContribution
from ._widgets import WidgetContribution
from ._writers import WriterContribution

__all__ = [
    "CommandContribution",
    "ContributionPoints",
    "KeyBindingContribution",
    "MenuItem",
    "ReaderContribution",
    "SampleDataContribution",
    "SampleDataGenerator",
    "SampleDataURI",
    "SubmenuContribution",
    "ThemeContribution",
    "WidgetContribution",
    "WriterContribution",
]


class ContributionPoints(BaseModel):
    commands: Optional[List[CommandContribution]]
    readers: Optional[List[ReaderContribution]]
    writers: Optional[List[WriterContribution]]
    widgets: Optional[List[WidgetContribution]]
    sample_data: Optional[List[SampleDataContribution]]
    themes: Optional[List[ThemeContribution]]
    menus: Dict[str, List[MenuItem]] = Field(
        default_factory=dict,
        description="Add menu items to existing napari menus."
        "A menu item can be a command, such as open a widget, or a submenu."
        "Using menu items, nested hierarchies can be created within napari menus."
        "This allows you to organize your plugin's contributions within"
        "napari's menu structure.",
    )
    submenus: Optional[List[SubmenuContribution]]
    keybindings: Optional[List[KeyBindingContribution]] = Field(None, hide_docs=True)

    configuration: List[ConfigurationContribution] = Field(
        default_factory=list,
        hide_docs=True,
        description="Configuration options for this plugin."
        "This section can either be a single object, representing a single category of"
        "settings, or an array of objects, representing multiple categories of"
        "settings. If there are multiple categories of settings, the Settings editor"
        "will show a submenu in the table of contents for that extension, and the title"
        "keys will be used for the submenu entry names.",
    )

    @validator("configuration", pre=True)
    def _to_list(cls, v):
        return v if isinstance(v, list) else [v]
