# coding: utf-8
from __future__ import annotations
from typing import Any, List, TYPE_CHECKING
from ..utils.type_var import PathOrStr
if TYPE_CHECKING:
    from ..events.args.event_args import EventArgs


class MissingInterfaceError(Exception):
    """Error when a interface is not found for a uno object"""

    def __init__(self, interface: Any, message: Any = None, *args) -> None:
        """
        MissingInterfaceError constructor

        Args:
            interface (Any): Missing Interface that caused error
            message (Any, optional): Message of error
        """
        if message is None:
            try:
                message = f"Missing interface {interface.__pyunointerface__}"
            except AttributeError:
                message = "Missing Uno Interface Error"
        super().__init__(interface, message, *args)

    def __str__(self) -> str:
        return repr(self.args[1])


class CellError(Exception):
    """Cell error"""

    pass


class ConfigError(Exception):
    """Config Error"""

    pass


class PropertyError(Exception):
    """
    Property Error
    """

    def __init__(self, prop_name: str, *args: object) -> None:
        """
        PropertyError Constructor

        Args:
            prop_name (str): Property name that caused error
        """
        super().__init__(prop_name, *args)

    def __str__(self) -> str:
        return repr(f"Property Error for: {self.args[0]}")


class PropertiesError(Exception):
    """Error for multiple properties"""
    pass


class PropertyNotFoundError(PropertyError):
    """Property Not Found Error"""

    def __str__(self) -> str:
        return repr(f"Property not found for: {self.args[0]}")


class GoalDivergenceError(Exception):
    """Error when goal seek result divergence is too high"""

    def __init__(self, divergence: float, message: Any = None) -> None:
        """
        GoalDivergenceError Constructor

        Args:
            divergence (float): divergence amount
            message (Any, optional): Message of error
        """
        if message is None:
            message = f"Divergence error: {divergence:.4f}"
        super().__init__(divergence, message)

    def __str__(self) -> str:
        return repr(self.args[1])


class UnKnownError(Exception):
    """Error for unknown results"""
    pass


class UnOpenableError(Exception):
    def __init__(self, fnm: PathOrStr, *args: object) -> None:
        """
        PropertyError Constructor

        Args:
            fnm (PathOrStr): File path that is not able to be opened.
        """
        super().__init__(fnm, *args)

    def __str__(self) -> str:
        return repr(f"Un-openable file: '{self.args[0]}'")

class MultiError(Exception):
    """Handles Multiple errors"""
    def __init__(self, errors: List[Exception]) -> None:
        """
        MultiError Constructor

        Args:
            errors (List[Exception]): List of errors
        """
        self.errors = errors
        super().__init__(self.errors)

    def __str__(self) -> str:
        return "\n".join([str(x) for x in self.errors])


class NotSupportedServiceError(Exception):
    """
    Handles errors of service not being supported.
    """
    def __init__(self, service_name: str, *args: object) -> None:
        """
        NotSupportedServiceError Constructor

        Args:
            service_name (str): Service name
        """
        super().__init__(service_name, *args)

    def __str__(self) -> str:
        return repr(f"Service not supported: '{self.args[0]}'")

class NotSupportedMacroModeError(Exception):
    """
    Handles errors of operations that are not allow when running as a macro.
    
    This error is largely used for methods that require external imports
    such as XML.apply_xslt()
    """
    pass

class CreateInstanceError(Exception):
    """Create instance Error"""
    def __init__(self, interface: Any, service: str, message: Any = None, *args) -> None:
        """
        constructor

        Args:
            interface (Any): Interface that failed creation
            message (Any, optional): Message of error
        """
        if message is None:
            message = f"Unable to create instance of {service}"
        super().__init__(interface, service, message, *args)

    def __str__(self) -> str:
        try:
            interface_name = self.args[0].__pyunointerface__
        except AttributeError:
            interface_name = "Unknown Interface"
        return f"Unable to create instance for service '{self.args[1]}' with interface of '{interface_name}'.\n{self.args[2]}"

class CreateInstanceMsfError(CreateInstanceError):
    """Create MSF Instance Error"""
    pass

class CreateInstanceMcfError(CreateInstanceError):
    """Create MCF Instance Error"""
    pass

class CancelEventError(Exception):
    """Error when an Event is canceled"""

    def __init__(self, event_args: EventArgs, message: Any = None, *args) -> None:
        """
        Cancel Event Error constructor

        Args:
            event_args (EventArgs): Event args that was canceled
            message (Any, optional): Message of error
        """
        if message is None:
            message = f"Event '{event_args.event_name}' is canceled!"
        super().__init__(event_args, message, *args)

    def __str__(self) -> str:
        return repr(self.args[1])

class CursorError(Exception):
    """Handles Cursor errors"""
    pass

class WordCursorError(CursorError):
    """Handles Word Cursor errors"""
    pass

class LineCursorError(CursorError):
    """Handles Line Cursor errors"""
    pass

class SentenceCursorError(CursorError):
    """Handles Sentence Cursor errors"""
    pass

class ParagraphCursorError(CursorError):
    """Handles Sentence Cursor errors"""
    pass

class PageCursorError(Exception):
    """Handles Page Cursor errors"""
    pass

class ViewCursorError(CursorError):
    """Handles View Cursor errors"""
    pass

class LoNotLoadedError(Exception):
    """Error when accessing Lo before Lo.load_office is called"""
    pass