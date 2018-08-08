import json
from random import randint

from faker import Faker
from faker.providers import BaseProvider

from wagtail.images.models import Image

# Grab all the ids of images so we can generate image fields at random
image_ids = list(Image.objects.values_list('id', flat=True))

fake = Faker()


def generate_field(field_type, value):
    return {
        'type': field_type,
        'value': value,
        'id': fake.uuid4(),
    }


def generate_paragraph_field():
    paragraphs = (
        f'<h3>{fake.sentence()}</h3>'
        f'<p>{fake.paragraph(nb_sentences=6, variable_nb_sentences=True)}</p>'
        f'<ul><li>{fake.word()}</li><li>{fake.word()}</li><li>{fake.word()}</li><li>{fake.word()}</li></ul>'
        f'<a href="{fake.url(schemes=["https"])}">Link to a fake url</a>'
    )

    return generate_field('paragraph', ''.join(paragraphs))


def generate_header_field():
    value = ' '.join(fake.words())

    return generate_field('header', value)


def generate_image_field():
    image_id = image_ids[randint(0, len(image_ids) - 1)]
    alt_text = ' '.join(fake.words(nb=5))
    caption = ' '.join(fake.words(nb=5))
    caption_url = fake.url(schemes=['https'])

    return generate_field('image', {
        'image': image_id,
        'altText': alt_text,
        'caption': caption,
        'captionURL': caption_url,
    })


def generate_image_text2_field():
    image_id = image_ids[randint(0, len(image_ids) - 1)]
    image_text = fake.paragraph(nb_sentences=1, variable_nb_sentences=False)
    url = fake.url(schemes=['https'])
    alt_text = ' '.join(fake.words(nb=5))
    small = fake.boolean()

    return generate_field('image_text2', {
        'image': image_id,
        'text': image_text,
        'url': url,
        'altText': alt_text,
        'small': small,
    })


def generate_grid_item():
    image_id = image_ids[randint(0, len(image_ids) - 1)]
    caption = fake.paragraph(nb_sentences=1)
    url = fake.url()

    return {
        'image': image_id,
        'caption': caption,
        'url': url,
    }


def generate_figuregrid2_field():
    image_count = randint(1, 9)
    grid_items = [generate_grid_item() for i in range(image_count)]

    return generate_field('figuregrid2', {
        'grid_items': grid_items
    })


def generate_spacer_field():
    size = randint(1, 5)

    return generate_field('spacer', {
        'size': size
    })


class StreamfieldProvider(BaseProvider):
    """
    A custom Faker Provider for relative image urls, for use with factory_boy

    >>> from factory import Faker
    >>> from networkapi.utility.faker import StreamfieldProvider
    >>> fake = Faker()
    >>> Faker.add_provider(StreamfieldProvider)
    """

    def streamfield(self, fields=None):
        """
        Generate a streamfield string containing the fields optionally defined in field_list
        """

        valid_fields = {
            'header': generate_header_field,
            'paragraph': generate_paragraph_field,
            'image': generate_image_field,
            'spacer': generate_spacer_field,
            'image_text2': generate_image_text2_field,
            'figuregrid2': generate_figuregrid2_field
        }

        streamfield_data = []

        # Default to a header and paragraph
        if not fields:
            fields = ['header', 'paragraph']

        for field in fields:
            if field in valid_fields:
                streamfield_data.append(valid_fields[field]())
            else:
                raise Exception(f'unknown field: {field}')

        return json.dumps(streamfield_data)
