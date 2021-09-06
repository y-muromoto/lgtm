import click


@click.command()
@click.option('--message', '-m', default='LGTM',
    show_default=True, help='画像に乗せるメッセージ')
@click.argument('keyword')
def cli():
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm') # 動作確認用


def lgtm(keyword, message):
    # 此処にロジックを」追加していく
    pass