from dip.ui import Application, Form, SpinBox


# Every application needs an Application.
app = Application()

# Create the model.
model = dict(name="Joe User", age=30)

# Define the view.
view_factory = Form('name', SpinBox('age', suffix=" years"),
        title="Configure Views")

# Create an instance of the view for the model.
view = view_factory(model)

# Make the instance of the view visible.
view.visible = True

# Enter the event loop.
app.execute()

# Show the value of the model.
print("Name:", model['name'])
print("Age:", model['age'])
