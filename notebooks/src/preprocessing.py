from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, TargetEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pandas as pd


def build_preprocessor(df_train, y):
    """
    Xây dựng và fit preprocessor chỉ trên tập train.
    """
    # ==== Nhóm cột theo loại xử lý ====
    num_features = ["age", "result"]
    binary_features = [f"A{i}_Score" for i in range(1, 11)]

    label_features = ["gender", "jaundice", "austim", "used_app_before", "age_desc"]
    target_features = ["ethnicity", "contry_of_res", "relation"]

    #Thứ tự của age_desc tăng dần
    age_desc_values = ['child', 'teen', 'young adult', 'adult', 'elderly']

    label_categories = [df_train[v].unique() for v in label_features[:4]]
    label_categories.append(age_desc_values)
    # ==== Pipeline con ====
    num_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    label_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder(categories=label_categories))
    ])

    target_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", TargetEncoder())
    ])

    # ==== ColumnTransformer ====
    preprocessor = ColumnTransformer([
        ("num", num_transformer, num_features),
        ("label", label_transformer, label_features),
        ("target", target_transformer, target_features),
        ("binary", "passthrough", binary_features)
    ])

    # Fit preprocessor chỉ trên train
    preprocessor.fit(df_train, y)

    return preprocessor


