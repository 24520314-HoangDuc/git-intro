from test_data import *
from policy import POLICY

def json_search(key, input_object, role=None):
    # 1. Nếu không truyền role, mặc định gán là "viewer"
    if role is None:
        role = "viewer"
        
    # 2. Lấy danh sách các role được phép truy cập key từ policy
    allowed_roles = POLICY.get(key, ())
    
    # 3. Nếu role hiện tại không nằm trong danh sách được phép, trả về mảng rỗng []
    if role not in allowed_roles:
        return []

    ret_val = []
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                ret_val.append({k: v})
            if isinstance(v, (dict, list)):
                ret_val.extend(json_search(key, v, role))
    elif isinstance(input_object, list):
        for item in input_object:
            if isinstance(item, (dict, list)):
                ret_val.extend(json_search(key, item, role))
    return ret_val
