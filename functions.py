def get_heroes_and_villains_relationships():
    query = """
        SELECT
            h1.name AS hero_name,
            h2.name AS villain_name,
            rlt.name AS relationship_type,
            a.name AS ability
        FROM
            relationships rel
        INNER JOIN
            heroes h1 ON rel.hero1_id = h1.id
        INNER JOIN
            heroes h2 ON rel.hero2_id = h2.id
        INNER JOIN
            relationship_types rlt ON rel.relationship_type_id = rlt.id
        LEFT JOIN
            abilities ab ON h1.id = ab.hero_id
        LEFT JOIN
            ability_types a ON ab.ability_type_id = a.id
        ORDER BY
            hero_name, villain_name;
    """
    returned_items = execute_query(query).fetchall()
    return returned_items