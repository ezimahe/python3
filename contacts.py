contacts = {
    'number' : 4,
    'students':
        [
            {'name': 'Eleanor Ezimah', 'email': 'eezimah@example.com'},
            {'name': 'Chichi Ezi', 'email': 'cezi@example.com'},
            {'name': 'Meso Mah', 'email': 'mmah@example.com'},
            {'name': 'Elle Ez', 'email': 'el@example.com'}
        ]
}

print('student emails')
for student in contacts['students']:
    print(student['email'])
