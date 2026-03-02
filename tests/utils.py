import hashlib

import pandas as pd


def generate_identifier(
        value,
        class_type,
        length=16,
):
    value_str = str(value)
    hash_object = hashlib.sha256(value_str.encode())
    hash_digest = hash_object.hexdigest()[:length]
    return f"{class_type.name}:{hash_digest}"

def create_individual_from_df_cell(
        cell,
        class_type,
):

    # If the pandas cell is null, return an empty individual
    if pd.isna(cell):
        return None

    # If the cell is an empty string, return an empty individual
    if cell == "":
        return None

    # Generate an identifier
    identifier = generate_identifier(value=cell, class_type=class_type)

    # Create the individual with the identifier
    individual = class_type(identifier)

    # Return the individual
    return individual

def create_triple(
        subject,
        predicate,
        object,
):

    if subject is None or object is None:
        return None

    predicate[subject].append(object)
    return predicate