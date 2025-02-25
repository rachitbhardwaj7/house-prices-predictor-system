import click
from pipelines.deployment_pipeline import (
    continuous_deployment_pipeline,
    inference_pipeline,
)
from rich import print
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)


@click.command()
@click.option(
    "--stop-service",
    is_flag=True,
    default=False,
    help="Stop the prediction service when done",
)
def run_main(stop_service: bool):
    """Run the prices predictor deployment pipeline"""
    model_name = "prices_predictor"

    model_deployer = MLFlowModelDeployer.get_active_model_deployer()

    if stop_service:
        existing_services = model_deployer.find_model_server(
            pipeline_name="continuous_deployment_pipeline",
            pipeline_step_name="mlflow_model_deployer_step",
            model_name=model_name,
            running=True,
        )

        if existing_services:
            print("[bold yellow]Stopping existing MLflow model server...[/bold yellow]")
            existing_services[0].stop(timeout=10)
        else:
            print("[bold red]No active MLflow model server found.[/bold red]")
        return

    print("[bold green]Running the Continuous Deployment Pipeline...[/bold green]")
    continuous_deployment_pipeline()

    print("[bold green]Running the Inference Pipeline...[/bold green]")
    inference_pipeline()

    print(
        "[bold blue]Now run:[/bold blue]\n"
        f"    mlflow ui --backend-store-uri {get_tracking_uri()}\n"
        "To inspect your experiment runs in MLflow UI."
    )

    service = model_deployer.find_model_server(
        pipeline_name="continuous_deployment_pipeline",
        pipeline_step_name="mlflow_model_deployer_step",
    )

    if service:
        print(f"[bold green]The MLflow prediction server is running at: {service[0].prediction_url}[/bold green]\n")
        print("To stop the service, re-run this command with `--stop-service`.")

if __name__ == "__main__":
    run_main()
