from oarepo_oai_pmh_harvester.decorators import rule
from oarepo_oai_pmh_harvester.transformer import OAITransformer
from oarepo_taxonomies.utils import get_taxonomy_json


@rule("nusl", "marcxml", "/998__/a", phase="pre")
def call_provider(el, **kwargs):
    return provider(el, **kwargs)  # pragma: no cover


def provider(el, **kwargs):
    slug = provider_mapping().get(el)
    if not slug:  # pragma: no cover
        return OAITransformer.PROCESSED
    return {
        "provider": get_taxonomy_json(code="institutions",
                                      slug=slug).paginated_data
    }


def provider_mapping():
    return {
        "agritec": "48392952",
        "agrotest_fyto": "25328859",
        "akademie_muzickych_umeni_v_praze": "61384984",
        "akademie_vytvarnych_umeni": "60461446",
        "archeologicky_ustav_brno": "68081758",
        "archeologicky_ustav_praha": "67985912",
        "archip": "28881699",
        "archiv_ing_arch_jana_moucky": "moucka",
        "archiv_doc_jiri_soucek": "soucek",
        "arnika": "26543281",
        "astronomicky_ustav": "67985815",
        "biofyzikalni_ustav": "68081707",
        "biologicke_centrum": "60077344",
        "biotechnologicky_ustav": "86652036",
        "botanicky_ustav": "67985939",
        "cenia": "45249130",
        "centrum_dopravniho_vyzkumu": "44994575",
        "centrum_pro_dopravu_a_energetiku": "67980961",
        "centrum_pro_regionalni_rozvoj": "04095316",
        "centrum_pro_studium_vysokeho_skolstvi": "00237752",
        "centrum_pro_vyzkum_verejneho_mineni": "68378025-cvvm",
        "centrum_vyzkumu_globalni_zmeny": "86652079",
        "ceska_asociace_ergoterapeutu": "62348451",
        "ceska_asociace_paraplegiku": "00473146",
        "ceska_narodni_banka": "48136450",
        "ceska_spolecnost_ornitologicka": "49629549",
        "ceska_zemedelska_univerzita": "60460709",
        "cesky_statisticky_urad": "00025593",
        "chmelarsky_institut": "14864347",
        "clovek_v_tisni": "25755277",
        "crdm": "68379439",
        "cvut": "68407700",
        "ekodomov": "26664488",
        "entomologicky_ustav": "60077344-entu",
        "etnologicky_ustav": "68378076",
        "evropske_hodnoty": "26987627",
        "fairtrade_cz_sk": "71226672",
        "filosoficky_ustav": "67985955",
        "fyzikalni_ustav": "68378271",
        "fyziologicky_ustav": "67985823",
        "galerie_vytvarneho_umeni_v_ostrave": "00373231",
        "gender_studies": "25737058",
        "geofyzikalni_ustav": "67985530",
        "geologicky_ustav": "67985831",
        "gle": "28204409",
        "hestia": "67779751",
        "historicky_ustav": "67985963",
        "hydrobiologicky_ustav": "60077344-hbu",
        "institut_umeni": "00023205",
        "iuridicum_remedium": "26534487",
        "jihoceska_univerzita_v_ceskych_budejovicich": "60076658",
        "jihomoravske_muzeum_ve_znojme": "00092738",
        "knihovna_av_cr": "67985971",
        "masarykova_univerzita": "00216224",
        "masarykuv_ustav_a_archiv": "67985921",
        "matematicky_ustav": "67985840",
        "mendelova_univerzita_v_brne": "62156489",
        "mikrobiologicky_ustav": "61388971",
        "ministerstvo_obrany": "60162694",
        "ministerstvo_spravedlnosti": "00025429",
        "ministerstvo_zivotniho_prostredi": "00164801",
        "moravska_galerie": "00094871",
        "moravska_zemska_knihovna": "00094943",
        "muzeum_brnenska": "00089257",
        "muzeum_vychodnich_cech": "00088382",
        "nacr": "70979821",
        "nadace_promeny": "27421538",
        "narodni_informacni_a_poradenske_stredisko_pro_kulturu": "14450551",
        "narodni_knihovna": "00023221",
        "narodni_lekarska_knihovna": "00023825",
        "narodni_muzeum": "00023272",
        "narodni_muzeum_v_prirode": "00098604",
        "narodni_pamatkovy_ustav": "75032333",
        "narodni_technicka_knihovna": "61387142",
        "narodni_technicke_muzeum": "00023299",
        "narodni_zemedelske_muzeum": "75075741",
        "narodohospodarsky_ustav": "67985998",
        "nulk": "00094927",
        "nuv": "00022179",
        "orientalni_ustav": "68378009",
        "oseva": "26791251",
        "ostravska_univerzita": "61988987",
        "pamatnik_narodniho_pisemnictvi": "00023311",
        "parazitologicky_ustav": "60077344-pau",
        "parlamentni_institut": "parlamentni_institut",
        "prague_college": "27164004",
        "psychologicky_ustav": "68081740",
        "sdruzeni_pro_integraci_a_migraci": "26612933",
        "severoceske_muzeum_v_liberci": "00083232",
        "siriri": "27447669",
        "slezske_zemske_muzeum": "00100595",
        "slovansky_ustav": "68378017",
        "sociologicky_ustav": "68378025",
        "surao": "66000769",
        "szpi": "75014149",
        "technologicke_centrum": "60456540",
        "ujep": "44555601",
        "umeleckoprumyslove_museum": "00023442",
        "univerzita_karlova_v_praze": "00216208",
        "upce": "00216275",
        "urad_prumysloveho_vlastnictvi": "48135097",
        "ustav_analyticke_chemie": "68081715",
        "ustav_anorganicke_chemie": "61388980",
        "ustav_archeologicke_pamatkove_pece_severozapadnich_cech": "47325011",
        "ustav_biologie_obratlovcu": "68081766",
        "ustav_chemickych_procesu": "67985858",
        "ustav_dejin_umeni": "68378033",
        "ustav_experimentalni_botaniky": "61389030",
        "ustav_experimentalni_mediciny": "68378041",
        "ustav_fotoniky_a_elektroniky": "67985882",
        "ustav_fyzikalni_chemie_j_heyrovskeho": "61388955",
        "ustav_fyziky_atmosfery": "68378289",
        "ustav_fyziky_materialu": "68081723",
        "ustav_fyziky_plazmatu": "61389021",
        "ustav_geoniky": "68145535",
        "ustav_informatiky": "67985807",
        "ustav_jaderne_fyziky": "61389005",
        "ustav_makromolekularni_chemie": "61389013",
        "ustav_molekularni_biologie_rostlin": "60077344-umbr",
        "ustav_molekularni_genetiky": "68378050",
        "ustav_organicke_chemie_a_biochemie": "61388963",
        "ustav_pristrojove_techniky": "68081731",
        "ustav_pro_ceskou_literaturu": "68378068",
        "ustav_pro_elektrotechniku": "61388998-ue",
        "ustav_pro_hydrodynamiku": "67985874",
        "ustav_pro_jazyk_cesky": "68378092",
        "ustav_pro_soudobe_dejiny": "68378114",
        "ustav_pro_studium_totalitnich_rezimu": "75112779",
        "ustav_pudni_biologie": "60077344-upb",
        "ustav_statu_a_prava": "68378122",
        "ustav_struktury_a_mechaniky_hornin": "67985891",
        "ustav_teoreticke_a_aplikovane_mechaniky": "68378297",
        "ustav_teorie_informace_a_automatizace": "67985556",
        "ustav_termomechaniky": "61388998",
        "ustav_zivocisne_fyziologie_a_genetiky": "67985904",
        "vscht": "60461373",
        "vugtk": "00025615",
        "vutbr": "00216305",
        "vuv_tgm": "00020711",
        "vvud": "00014125",
        "vysoka_skola_ekonomicka_v_praze": "61384399",
        "vysoka_skola_evropskych_a_regionalnich_studii": "26033909",
        "vysoka_skola_financni_a_spravni": "04274644",
        "vysoka_skola_manazerske_informatiky_a_ekonomiky": "04130081",
        "vyzkumny_ustav_bezpecnosti_prace": "00025950",
        "vyzkumny_ustav_lesniho_hospodarstvi_a_myslivosti": "00020702",
        "vyzkumny_ustav_potravinarsky": "00027022",
        "vyzkumny_ustav_prace_a_socialnich_veci": "45773009",
        "vyzkumny_ustav_rostlinne_vyroby": "00027006",
        "vyzkumny_ustav_silva_taroucy": "00027073",
        "woodexpert": "28282027",
        "zapadoceska_univerzita": "49777513",
        "zapadoceske_muzeum_v_plzni": "00228745"
    }
