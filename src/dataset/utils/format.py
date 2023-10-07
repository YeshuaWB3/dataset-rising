import io
import json
import random
from typing import List, Optional

from database.entities.post import PostEntity

from .download import download_image
from .load import load_image
from .resize import resize_image


def format_posts_for_dataset(samples: List[str], limit: Optional[int], agent: str, image_width: int, image_height: int, image_format: str, image_quality: int, separator: str):
    if image_format.upper() == 'JPG' or image_format.upper() == '.JPG':
        image_format = 'JPEG'

    count = 0

    for sample_file in samples:
        if limit is not None and count >= limit:
            continue

        with open(sample_file, 'rt') as ap:
            for line in ap:
                if limit is not None and count >= limit:
                    continue

                post = PostEntity(post=json.loads(line))
                download = download_image(post, agent)

                if download is None:
                    continue

                im = load_image(download, post)

                if im is None:
                    continue

                resized_image = resize_image(im=im, post=post, max_width=image_width, max_height=image_height)

                if resized_image is None:
                    continue

                # shuffle tags
                shuffled_tags = post.tags.copy()
                random.shuffle(shuffled_tags)

                # compress image
                compressed_image = io.BytesIO()
                resized_image.save(compressed_image, format=image_format, quality=image_quality, optimize=True)

                record = {
                    'source_id': post.source_id,
                    'source': post.source,
                    'image': compressed_image.getvalue(),
                    'tags': shuffled_tags,
                    'url': post.image_url,
                    'text': separator.join(shuffled_tags),
                    'desc': post.description,
                    'selector': post.selector
                }

                yield record
                count += 1

