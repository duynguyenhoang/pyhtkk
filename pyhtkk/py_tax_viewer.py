"""
Usage: python pyhtkk/py_tax_viewer.py YOUR_HTKK_OR_ONLINE_OUTPUT.xml

Default output will be .docx

"""
import sys

import xmltodict
from docxtpl import DocxTemplate


TPL_MAU02_QT_TNCN09 = './templates/MAU-02-QT-TNCN09.docx'
EMPTY_STRING = '......'


def str_or_default(str_val, default_str=EMPTY_STRING):
    """
    :param str_val:
    :param default_str:
    :return:
    """
    return str_val if str_val else default_str


def fmt_vnd(str_val):
    """
    Định dạng thành chuõi tiền tệ VN, ví dụ 1.203.400
    :param str_val:
    :return:
    """
    currency = '{:,.0f}'.format(float(str_val)).replace(',', '.')

    return currency


def load_data(file_name):
    """
    Đọc tập tin kê khai thuế xml
    :param file_name:
    :return:
    """
    with open(file_name, encoding='utf-8') as f:
        return xmltodict.parse(f.read())


def render_02qttncn09(data, doc_file):
    """
    Mẫu số 02/QTT-TNCN
    :param data:
    :param doc_file:
    :return:
    """
    thong_tin_khai_thue = data['HSoThueDTu']['HSoKhaiThue']['TTinChung']['TTinTKhaiThue']
    tttk = thong_tin_khai_thue['TKhaiThue']
    nnt = thong_tin_khai_thue['NNT']
    so_lan = int(tttk['soLan'])
    ky_ke_khai_thue = tttk['KyKKhaiThue']
    ctieu_to_khai = data['HSoThueDTu']['HSoKhaiThue']['CTieuTKhaiChinh']

    context = {
        'YEAR': ky_ke_khai_thue['kyKKhai'],
        'fThang': ky_ke_khai_thue['kyKKhaiTuThang'],
        'tThang': ky_ke_khai_thue['kyKKhaiDenThang'],
        'lanDau': 'X' if so_lan == 0 else '',
        'soLan': so_lan if so_lan > 0 else '',
        'tenNNT': nnt['tenNNT'],
        'mst': nnt['mst'],
        'dchiNNT': nnt['dchiNNT'],
        'tenHuyenNNT': nnt['tenHuyenNNT'],
        'tenTinhNNT': nnt['tenTinhNNT'],
        'dthoaiNNT': nnt['dthoaiNNT'],
        'faxNNT': str_or_default(nnt['faxNNT']),
        'emailNNT': str_or_default(nnt['emailNNT']),
        'tkNH': str_or_default(ctieu_to_khai['Header']['ct12']),
        'tenNH': str_or_default(ctieu_to_khai['Header']['ct12a']),
    }

    for i in range(22, 50):
        i_key = f'ct{i}'
        context[i_key] = fmt_vnd(ctieu_to_khai[i_key])

    render(TPL_MAU02_QT_TNCN09, context, doc_file)


def render(template_name, context, doc_file):
    """
    Xuất nội dung và lưu tập tin
    :param template_name:
    :param context:
    :param doc_file:
    :return:
    """
    file_path = f'{doc_file}.docx'
    doc = DocxTemplate(template_name)
    doc.render(context)
    doc.save(file_path)

    print(f'Saved file to {file_path}')


if __name__ == '__main__':
    _, file_path, *argv = sys.argv
    data = load_data(file_path)
    doc_file = '.'.join(file_path.split('.')[:-1])

    render_02qttncn09(data, doc_file)
