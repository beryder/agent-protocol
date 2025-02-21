# generated by fastapi-codegen:
#   filename:  openapi.json

from __future__ import annotations

from fastapi import APIRouter

from ..models import Agent, AgentSchemas, AgentsGetResponse, ErrorResponse, Union

router = APIRouter(tags=["Agents"])


@router.get(
    "/agents",
    response_model=AgentsGetResponse,
    responses={"404": {"model": ErrorResponse}, "422": {"model": ErrorResponse}},
    tags=["Agents"],
)
def list_agents_get_agents() -> Union[AgentsGetResponse, ErrorResponse]:
    """
    List Agents
    """
    pass


@router.get(
    "/agents/{agent_id}",
    response_model=Agent,
    responses={"404": {"model": ErrorResponse}},
    tags=["Agents"],
)
def get_agent_agents__agent_id__get(agent_id: str) -> Union[Agent, ErrorResponse]:
    """
    Get Agent
    """
    pass


@router.get(
    "/agents/{agent_id}/schemas",
    response_model=AgentSchemas,
    responses={"404": {"model": ErrorResponse}, "422": {"model": ErrorResponse}},
    tags=["Agents"],
)
def get_agent_schemas_agents__agent_id__schemas_get(
    agent_id: str,
) -> Union[AgentSchemas, ErrorResponse]:
    """
    Get Agent Schemas
    """
    pass
