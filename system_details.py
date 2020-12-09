import platform

u = platform.uname()

print(f'System: {u.system}')
print(u.node)
print(u.release)
print(u.version)
print(u.machine)
print(u.processor)
