# utils/table_utils.py
from rich.table import Table
from config_settings import activity_count, death_count, start_time
from datetime import datetime

def generate_table():
    elapsed_time = datetime.now() - start_time
    hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
    minutes, _ = divmod(remainder, 60)

    table = Table(title="Статистика")
    table.add_column("Активность", justify="right", style="cyan", no_wrap=True)
    table.add_column("Количество", style="magenta")

    for activity, count in activity_count.items():
        table.add_row(activity, str(count))
    table.add_row("Смерти", str(death_count))
    table.add_row("Общее время", f"{int(hours)} ч {int(minutes)} мин")

    return table