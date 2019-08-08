# python 3
def licenseKeyFormatting(license: str, groupSize: int) -> str:
    # count alphanumeric size
    size = sum(1 for c in license if c != '-') # 1n

    firstGroupSize = size % groupSize

    groupIndex = 0
    group = [''] * groupSize
    result = []

    for c in license: # 2n
        if c != '-':
            group[groupIndex] = c.upper()
            groupIndex += 1

            # first group ?
            if firstGroupSize != 0:
                if groupIndex == firstGroupSize:
                    result.append(''.join(group))
                    groupIndex = 0

                    # no more first group
                    firstGroupSize = 0
                    
            elif groupIndex == groupSize:
                result.append(''.join(group))
                groupIndex = 0

    return '-'.join(result) # 3n
