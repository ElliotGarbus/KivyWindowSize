# KivyWindowSize
Method for using the config facility for saving and restoring the window size and postion on Linux, Windows and Mac.  The application will open initially at a default position.  After closing the app the window position and size will be saved.  The next time the application is started it will be in the previous size and location.

The App class provides the on_stop event.  This is described as:

    Event handler for the on_stop event which is fired when the application has 
    finished running (i.e. the window is about to be closed).

On MSFT Windows, the values of Window.top and Window.left are NOT valid when the App.on_stop() event happens, but the size is valid.

The Kivy Window class instance has an event called, on_request_close(), this is called when the window close has been request, but prior to the window close. 

    Fired when the event loop wants to close the window, or if the escape key is pressed and exit_on_escape is True. 
    If a function bound to this event returns True, the window will not be closed. 
    If the the event is triggered because of the keyboard escape key, the keyword argument source is dispatched 
    along with a value of keyboard to the bound functions.

Under Windows, the size and position values are valid here.  I am capturing the size and position data at this event and
writing them into the config file at App.on_stop().


**Key Learnings:**
**Windows Size and Position are not valid at on_stop().**  The window size and position is not correct at this time so these value must be captured earlier.  The Kivy Window object has an event, on_request_close, binding to this event I can consistently capture size and position. This has been verified on Windows and Linux.

**Needed to use configparser and Config.set() prior to loading Kivy.app**  I needed to use python's config object to access the .ini file so I could set the Window Size and position prior to loading Kivy.app.  Without doing this, a blank window would draw as defined by the Kivy settings, then jump to the place defined in on_start.

**The Window event on_draw is called on resize and position change on Windows but not Linux.** On Linux on_draw is only called on resize

**Window size is effected by Metrics.density**  The window size is automatically adjusted based on Metrics.density on macOS machines.  When saving the window size to the .ini file, the Window.size must be divided by Metrics.density.  If this not done, and metrics.density == 2, for example, the window size will double each time the program is opened.

Note: This is a simple test program.  There are 2 text input fields, no validation is done on the input.  Integers must be entered for proper operation.  Enter the desired window size and press the button, and the window will resize.  On some machines the the kivy metric dp() will result in the same size, on other machines (Mac for example) the size will be different.
