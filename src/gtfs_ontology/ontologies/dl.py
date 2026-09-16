from gtfs_ontology.ontologies import *

# region Add the datatypes to comply with DL profile.

with gtfs:

    # g.add((XSD.date, RDF.type, RDFS.Datatype))
    # g.add((XSD.time, RDF.type, RDFS.Datatype))

    class color(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^[0-9A-F]{6}$")
        ]
    g.add((URIRef(color.iri), RDFS.label, Literal("color", "en")))

    class currency_code(Datatype):
        dfs = pd.read_html("https://en.wikipedia.org/wiki/ISO_4217#Active_codes",
                           storage_options={'User-Agent': 'Mozilla/5.0'})
        equivalent_to = [OneOf(dfs[1]["Code"].tolist())]
    g.add((URIRef(currency_code.iri), RDFS.label, Literal("currency code", "en")))

    class currency_amount(Datatype):
        pass
    g.add((URIRef(currency_amount.iri), RDFS.label, Literal("currency amount", "en")))
    g.add((URIRef(id.iri), OWL.equivalentClass, XSD.string))

    class dateType(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$")
        ]
    g.add((URIRef(dateType.iri), RDFS.label, Literal("date", "en")))

    class email(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        ]
    g.add((URIRef(email.iri), RDFS.label, Literal("email", "en")))

    class id(Datatype):
        pass
    g.add((URIRef(id.iri), RDFS.label, Literal("id", "en")))
    g.add((URIRef(id.iri), OWL.equivalentClass, XSD.string))

    class language_code(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")
        ]
    g.add((URIRef(language_code.iri), RDFS.label, Literal("language code", "en")))

    class latitude(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=float, min_inclusive=-90, max_inclusive=90)
        ]
    g.add((URIRef(language_code.iri), RDFS.label, Literal("latitude", "en")))

    class longitude(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=float, min_inclusive=-180, max_inclusive=180)
        ]
    g.add((URIRef(language_code.iri), RDFS.label, Literal("longitude", "en")))

    class nonNegativeFloat(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=float, min_inclusive=0)
        ]
    g.add((URIRef(nonNegativeFloat.iri), RDFS.label, Literal("non-negative float", "en")))

    class phone_number(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\+?[1-9]\d{1,14}$")
        ]
    g.add((URIRef(phone_number.iri), RDFS.label, Literal("phone number", "en")))

    class time(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\d+:[0-5]\d:[0-5]\d$")
        ]
    g.add((URIRef(time.iri), RDFS.label, Literal("time", "en")))

    class local_time(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\d+:[0-5]\d:[0-5]\d$")
        ]
    g.add((URIRef(local_time.iri), RDFS.label, Literal("local time", "en")))

    class text(Datatype):
        pass
    g.add((URIRef(text.iri), RDFS.label, Literal("text", "en")))
    g.add((URIRef(text.iri), OWL.equivalentClass, XSD.string))

    class timezone(Datatype):
        dfs = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones",
            storage_options={'User-Agent': 'Mozilla/5.0'})
        equivalent_to = [OneOf(dfs[0][('TZ identifier', 'TZ identifier')].tolist())]
    g.add((URIRef(timezone.iri), RDFS.label, Literal("timezone", "en")))

    class url(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^https?:\/\/(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\/[^\s]*)?$")
        ]
    g.add((URIRef(url.iri), RDFS.label, Literal("url", "en")))

with gtfs:

    agency_id.range = [id]
    agency_name.range = [text]
    agency_url.range = [url]
    agency_timezone.range = [timezone]
    agency_lang.range = [language_code]
    agency_phone.range = [phone_number]
    agency_fare_url.range = [url]
    agency_email.range = [email]
    cemv_support.range = [OneOf([0, 1, 2])]