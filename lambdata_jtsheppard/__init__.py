ZEROS = np.zeros(5)
ONES = np.ones(10)

def train_validation_test_split(
    X, y, train_size=0.7, val_size=0.1, test_size=0.2, 
    random_state=None, shuffle=True):
        
    assert train_size + val_size + test_size == 1
    
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size/(train_size+val_size), 
        random_state=random_state, shuffle=shuffle)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

def stringer(df,filename):
    '''Takes in df and filename converts ID column to string, creates con_id using stringified id and filename
    returns returns id column to int '''
    dfc = df.copy()
    st = []
    con_id = []
    for x in dfc.id:
        st.append(str(x))
    for f in st:
        id.append(filename + f)
    dfc["id"] = id