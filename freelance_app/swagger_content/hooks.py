
def preprocessing_filter_account(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        # Выводите только EndPoints для аккаунта
        if 'api/freelance_app/account' in path:
            filtered.append((path, path_regex, method, callback))
    return filtered