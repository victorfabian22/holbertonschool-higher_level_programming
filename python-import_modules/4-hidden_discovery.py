#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for name in names:
        if name[0] != '_':
            print(name)
