class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replacements_map = {}
        for key, value in replacements:
            replacements_map[key] = value
        
        def get_value(key):
            val = replacements_map[key]
            while "%" in val:
                for k, v in replacements_map.items():
                    val = val.replace(f"%{k}%", v)
            return val

        text_list = text.split("_")
        for idx, e in enumerate(text_list):
            text_list[idx] = get_value(e[1:-1])
        return "_".join(text_list)