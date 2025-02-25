import click
from pipelines.training_pipeline import ml_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from rich import print


@click.command()
def main():
    """
    Run the ML pipeline and start the MLflow UI for experiment tracking.
    """
    print("[bold green]Running the ML Training Pipeline...[/bold green]")

    try:
        ml_pipeline()
        print("[bold cyan]Pipeline executed successfully![/bold cyan]")
    except Exception as e:
        print(f"[bold red]Error during pipeline execution: {e}[/bold red]")
        return

    print(
        "[bold blue]Now run:[/bold blue]\n"
        f"    mlflow ui --backend-store-uri '{get_tracking_uri()}'\n"
        "To inspect your experiment runs in MLflow UI."
    )


if __name__ == "__main__":
    main()
