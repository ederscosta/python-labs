def add_setting(test_settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

def update_setting(test_settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(test_settings, key):
    key = key.lower()

    if key in test_settings:
        test_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'


def view_settings(test_settings):
    if not test_settings:
        return 'No settings available.'

    user_info = 'Current User Settings:\n'

    for key, value in test_settings.items():
        key = key.capitalize()
        user_info += f"{key}: {value}\n"

    return user_info