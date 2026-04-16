from gtfs_ontology.realtime.core import *

ACTIVE_PERIOD_DEF = """
Time when the alert should be shown to the user. If missing, the alert will be shown as long as it appears in the feed. If multiple ranges are given, the alert will be shown during all of them.
"""

INFORMED_ENTITY_DEF = """
Entities whose users we should notify of this alert. At least one informed_entity must be provided.
"""

CAUSE_DEF = """
If cause_detail is included, then Cause must also be included.
"""

CAUSE_DETAIL_DEF = """
Description of the cause of the alert that allows for agency-specific language; more specific than the Cause. If cause_detail is included, then Cause must also be included. 
"""

EFFECT_DEF = """
If effect_detail is included, then Effect must also be included.
"""

EFFECT_DETAIL_DEF = """
Description of the effect of the alert that allows for agency-specific language; more specific than the Effect. If effect_detail is included, then Effect must also be included. 
"""

URL_DEF = """
The URL which provides additional information about the alert.
"""

HEADER_TEXT_DEF = """
Header for the alert. This plain-text string will be highlighted, for example in boldface.
"""

DESCRIPTION_TEXT_DEF = """
Description for the alert. This plain-text string will be formatted as the body of the alert (or shown on an explicit "expand" request by the user). The information in the description should add to the information of the header.
"""

TTS_HEADER_TEXT_DEF = """
Text containing the alert's header to be used for text-to-speech implementations. This field is the text-to-speech version of header_text. It should contain the same information as header_text but formatted such that it can read as text-to-speech (for example, abbreviations removed, numbers spelled out, etc.)
"""

TTS_DESCRIPTION_TEXT_DEF = """
Text containing a description for the alert to be used for text-to-speech implementations. This field is the text-to-speech version of description_text. It should contain the same information as description_text but formatted such that it can be read as text-to-speech (for example, abbreviations removed, numbers spelled out, etc.)
"""

SEVERITY_LEVEL_DEF = """
Severity of the alert.
"""

IMAGE_DEF = """
TranslatedImage to be displayed along the alert text. Used to explain visually the alert effect of a detour, station closure, etc. The image should enhance the understanding of the alert and must not be the only location of essential information. The following types of images are discouraged : image containing mainly text, marketing or branded images that add no additional information. 
"""

IMAGE_ALTERNATIVE_TEXT_DEF = """
Text describing the appearance of the linked image in the image field (e.g., in case the image can't be displayed or the user can't see the image for accessibility reasons). 
"""

with gtfs:

    class Cause(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "UNKNOWN_CAUSE",
                    "OTHER_CAUSE",
                    "TECHNICAL_PROBLEM",
                    "STRIKE",
                    "DEMONSTRATION",
                    "ACCIDENT",
                    "HOLIDAY",
                    "WEATHER",
                    "MAINTENANCE",
                    "CONSTRUCTION",
                    "POLICE_ACTIVITY",
                    "MEDICAL_EMERGENCY",
                ]
            )
        ]

    class Effect(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "NO_SERVICE",
                    "REDUCED_SERVICE",
                    "SIGNIFICANT_DELAYS",
                    "DETOUR",
                    "ADDITIONAL_SERVICE",
                    "MODIFIED_SERVICE",
                    "OTHER_EFFECT",
                    "UNKNOWN_EFFECT",
                    "STOP_MOVED",
                    "NO_EFFECT",
                    "ACCESSIBILITY_ISSUE"
                ]
            )
        ]

    class SeverityLevel(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "UNKNOWN_SEVERITY",
                    "INFO",
                    "WARNING",
                    "SEVERE",
                ]
            )
        ]

    class active_period(FieldValue, FunctionalProperty):
        comment = [locstr(ACTIVE_PERIOD_DEF, "en")]
        domain = [Alert]
        range = [TimeRange]

    class informed_entity(FieldValue, FunctionalProperty):
        comment = [locstr(INFORMED_ENTITY_DEF, "en")]
        domain = [Alert]
        range = [EntitySelector]

    class cause(FieldValue, FunctionalProperty):
        comment = [locstr(CAUSE_DEF), "en"]
        domain = [Alert]
        range = [Cause]

    class cause_detail(ExperimentalField, FunctionalProperty):
        comment = [locstr(CAUSE_DETAIL_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]

    class effect(FieldValue, FunctionalProperty):
        comment = [locstr(EFFECT_DEF), "en"]
        domain = [Alert]
        range = [Effect]

    class effect_detail(ExperimentalField, FunctionalProperty):
        comment = [locstr(EFFECT_DETAIL_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]

    class url(FieldValue, FunctionalProperty):
        comment = [locstr(URL_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]

    class header_text(FieldValue, FunctionalProperty):
        comment = [locstr(HEADER_TEXT_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]

    class description_text(FieldValue, FunctionalProperty):
        comment = [locstr(DESCRIPTION_TEXT_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]

    class tts_header_text(FieldValue, FunctionalProperty):
        comment = [locstr(TTS_HEADER_TEXT_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]

    class tts_description_text(FieldValue, FunctionalProperty):
        comment = [locstr(TTS_DESCRIPTION_TEXT_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]

    class severity_level(FieldValue, FunctionalProperty):
        comment = [locstr(SEVERITY_LEVEL_DEF), "en"]
        domain = [Alert]
        range = [SeverityLevel]

    class image(ExperimentalField, FunctionalProperty):
        comment = [locstr(IMAGE_DEF), "en"]
        domain = [Alert]
        range = [TranslatedImage]

    class image_alternative_text(ExperimentalField, FunctionalProperty):
        comment = [locstr(IMAGE_ALTERNATIVE_TEXT_DEF), "en"]
        domain = [Alert]
        range = [TranslatedString]