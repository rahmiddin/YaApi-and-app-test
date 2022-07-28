import pytest
from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf
from main import add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf,move_doc_to_shelf, show_document_info,add_new_doc
from unittest.mock import patch


class TestFunc:

    @pytest.mark.parametrize(
        "number",
        [
            '2207 876234',
        ]
    )
    def test_cls_check_document_existance(self, number):
        """Это метод тестирования функции check_document_existance"""
        result = check_document_existance(number)
        assert result == True

    @patch('builtins.input', return_value='11-2')
    def test_cls_get_doc_owner_name(self, mock_input):
        result = get_doc_owner_name()
        assert result

    def test_cls_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        assert result

    def test_cls_remove_doc_from_shelf(self):
        result = remove_doc_from_shelf('10006')
        assert result == True

    def test_cls_add_new_shelf(self):
        result = add_new_shelf('4')
        assert result[1] == True

    @pytest.mark.parametrize(
        "shell",
        [
            {'1': ['2207 876234', '11-2', '5455 028765', '007']},
        ]
    )
    def test_cls_append_doc_to_shelf(self, shell):
        result = append_doc_to_shelf('1', '007')
        assert result['1'] == shell['1']

    @patch('builtins.input', return_value='11-2')
    def test_cls_delete_doc(self, mock_input):
        result = delete_doc()
        assert result[1] == True

    @patch('builtins.input', return_value='2207 876234')
    def test_cls_get_doc_shelf(self, mock_input):
        result = get_doc_shelf()
        assert result == '1'

    @patch('builtins.input', side_effect=['2207 876234', '4'])
    def test_cls_move_doc_to_shelf(self, mock_input):
        result = move_doc_to_shelf()
        assert 'перемещен' in result
    
    @pytest.mark.parametrize(
        "documents",
        [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
    )
    def test_cls_show_document_info(self, documents):
        result = show_document_info(documents)
        assert result[0] == documents['type']
        
    @patch('builtins.input', side_effect=['007', 'password', 'John', 2])
    def test_cls_add_new_doc(self, mock_input):
        result = add_new_doc()
        assert result == 2

