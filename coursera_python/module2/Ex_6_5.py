def extract_end_float(t):
    zero_pos = t.find("0")
    return float( t[zero_pos : ] )
