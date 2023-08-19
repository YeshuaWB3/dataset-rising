from utils.db_utils import connect_to_db

(db, client) = connect_to_db()

db_name = db.name

client.drop_database(db_name)
db = client[db_name]

posts = db.create_collection('posts')
posts.create_index(['source_id', 'source'], unique=True)
posts.create_index(['origin_urls'], unique=False, sparse=True)
posts.create_index(['tags'])
posts.create_index(['origin_md5'])
posts.create_index(['image_ratio'])

tags = db.create_collection('tags')
tags.create_index(['source_id', 'source'], unique=True)
tags.create_index(['count'])
tags.create_index(['category'])
tags.create_index(['origin_name', 'source'], unique=True)
tags.create_index(['reference_name', 'source'])
tags.create_index(['alternative_ids.source_id', 'alternative_ids.source'], unique=True, sparse=True)
tags.create_index(['v1_name'], unique=True)
tags.create_index(['v2_name'], unique=True)
tags.create_index(['v2_short'], unique=False)
tags.create_index(['preferred_name'], unique=True)

implications = db.create_collection('implications')
implications.create_index(['origin_name'], unique=False)
implications.create_index(['source_id', 'source'], unique=True)

translations = db.create_collection('translations')
translations.create_index(['source_id', 'source'], unique=True)
translations.create_index(['origin_name', 'source'], unique=True)
translations.create_index(['e621_name'], unique=True)
