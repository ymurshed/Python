from Helper import Helper
from FormMappingDS import FormMappingDS
import xml.etree.ElementTree as Et


class FormMappingXML(FormMappingDS):

    def __init__(self, fm):
        a = Et.Element('Form')
        b = Et.SubElement(a, 'QCATFormTemplateID')
        b.text = fm.qcat_form_template_id
        c = Et.SubElement(a, 'SFFormTemplateID')
        c.text = fm.sf_form_template_id
        d = Et.SubElement(a, 'FormName')
        d.text = fm.qcat_form_name
        e = Et.SubElement(a, 'FieldCount')
        e.text = str(fm.field_count)

        self.do_item_level_mapping(a, fm)

        tree = fm.comment + "\n"
        tree += Et.tostring(a).decode('utf-8')

        Helper.write_xml_file(fm.qcat_form_name + '-' + fm.file_name, tree)

    def do_item_level_mapping(self, a, fm):
        f = Et.SubElement(a, 'FormItems')
        x = 1
        while x <= fm.field_count:

            g = Et.SubElement(f, 'FormItem')
            h = Et.SubElement(g, 'QCATItemName')
            h.text = fm.qcat_item_names[x]
            i = Et.SubElement(g, 'SFItem')
            i.text = fm.sf_item_names[x]

            j = Et.SubElement(g, 'ItemValuesMapping')
            y = 0

            while y < len(fm.qcat_item_values[x]):
                k = Et.SubElement(j, 'ItemValueMap')
                l = Et.SubElement(k, 'QCATItemValue')
                l.text = fm.qcat_item_values[x][y]
                m = Et.SubElement(k, 'SFItemValue')
                m.text = fm.sf_item_values[x][y]
                y += 1
            x += 1


