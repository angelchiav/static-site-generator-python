from blocktype import BlockType

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if lines[0].startswith("#"):
        count = 0
        for ch in lines[0]:
            if ch == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and len(lines[0]) > count and lines[0][count] == " ":
            return BlockType.HEADING
        
    is_quote = True
    for line in lines:
        if not line.startswith("> "):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    
    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
            break
    if is_unordered:
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    expected_number = 1
    for line in lines:
        prefix = f"{expected_number}. "
        if not line.startswith(prefix):
            is_ordered = False
            break
        expected_number += 1
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH