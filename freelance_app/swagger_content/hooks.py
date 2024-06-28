
def preprocessing_filter_account(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        # Выводит только EndPoints для аккаунта
        if 'api/freelance_app/account' in path:
            filtered.append((path, path_regex, method, callback))
    return filtered


def preprocessing_filter_work(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        # Выводит только EndPoints для работы (услуги, заказы)
        if 'api/freelance_app/work' in path:
            filtered.append((path, path_regex, method, callback))
    return filtered