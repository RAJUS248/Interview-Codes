def lruchace(a,b):
    seen = {}
    size = 0

    for i in range(len(a)):

        if a[i] == "LRUCache":
            size = b[i][0]

        elif a[i] == "put":
            key, value = b[i]

            # If key exists → remove and reinsert (to mark recent)
            if key in seen:
                seen.pop(key)
            # If full → remove least recently used (first key)
            elif len(seen) >= size:
                first_key = next(iter(seen))
                del seen[first_key]

            # Add as most recent (at end)
            seen[key] = value

        elif a[i] == "get":
            key = b[i][0]

            if key in seen:
                # Move to end (most recent)
                value = seen.pop(key)
                seen[key] = value
                print(seen[key])
            
            else:
                print(-1)


a = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
b = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

lruchace(a,b)
