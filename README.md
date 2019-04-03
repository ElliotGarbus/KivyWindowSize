# KivyWindowSize
Method for saving and restoring the window size on Linux, Windows and Mac

The App class provides the on_stop event.  This is described as:

    Event handler for the on_stop event which is fired when the application has 
    finished running (i.e. the window is about to be closed).

On MSFT Windows, the values of Window.top and Window.left are NOT valid when the App.on_stop() event happens, but the size is valid.

The Window class instance has an event called, on_request_close(), this is called when the window close has been request, but prior to window close. 

    Fired when the event loop wants to close the window, or if the escape key is pressed and exit_on_escape is True. If a function bound to this event returns True, the window will not be closed. If the the event is triggered because of the keyboard escape key, the keyword argument source is dispatched along with a value of keyboard to the bound functions.

Under Windows, the size and position values are valid here.  I am capturing the size and position data at this event and writing them into the config file.


