#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import pathlib
from pathlib import Path
import json
import jsonschema
from jsonschema import validate
from prod_schema import schema


def add_product(products, prod, shop, cost):
    """
    Ввод информации о товарах.
    """
    products.append(
        {
            "product": prod,
            "shop": shop,
            "cost": cost
        }
    )
    return products


def save_products(path, products):
    """
    Сохранить список всех товаров в формате JSON
    """
    with open(path, "w", encoding="utf-8") as fout:
        json.dump(products, fout, ensure_ascii=False, indent=4)


def load_products(path):
    """
    Загрузить список всех товаров из файла JSON
    """
    with open(path, "r", encoding="utf-8") as fin:
        return json.load(fin)


def product_list(products):
    """
    Вывод списка товаров
    """
    if products:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20
        )
        print(line)
        print(
            '| {:^25} | {:^15} | {:^14} |'.format(
                "Товар",
                "Магазин",
                "Стоимость"
            )
        )
        print(line)

        for product in products:
            print(
                '| {:^25} | {:^15} | {:^14} |'.format(
                    product.get('product', ''),
                    product.get('shop', ''),
                    product.get('cost', 0)
                )
            )
            print(line)


def select(products, shop):
    """
    Выбрать товары из конкретного магазина.
    """
    result = []
    for product in products:
        if product.get('shop', '') == shop:
            result.append(product)
    return result


def validation(json_data):
    """
    Валидация данных
    """
    try:
        validate(instance=json_data, schema=schema)
    except:
        raise jsonschema.exceptions.ValidationError("Данные недействительны")

    msg = "Данные успешно загружены"
    return True, msg


def main(command_line=None):
    """
    Главная функция программы.
    """
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
        help="Путь к файлу"
    )

    parser = argparse.ArgumentParser("products")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Добавить новый продукт"
    )
    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
        help="Название продуктов"
    )
    add.add_argument(
        "-s",
        "--shop",
        action="store",
        help="Название магазина"
    )
    add.add_argument(
        "-c",
        "--cost",
        action="store",
        type=float,
        required=True,
        help="Стоимость товара"
    )

    list = subparsers.add_parser(
        "list",
        parents=[file_parser],
        help="Отобразить список товаров"
    )

    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
        help="Выбрать товары из магазина"
    )
    select.add_argument(
        "-s",
        "--shop",
        action="store",
        type=str,
        required=True,
        help="Название магазина"
    )

    args = parser.parse_args(command_line)
    path = pathlib.Path.home() / args.filename

    is_dirty = False
    if path.exists:
        products = load_products(path)
    else:
        products = []

    match args.command:
        case 'add':
            products = add_product(
                products,
                args.name,
                args.shop,
                args.cost
            )
            is_dirty = True
        case 'list':
            product_list(products)
        case 'select':
            selected = select(products, args.shop)
            product_list(selected)

    if is_dirty:
        save_products(path, products)


if __name__ == '__main__':
    main()
