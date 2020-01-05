import React from 'react'
import "./styles.scss"
import Card from '@material-ui/core/Card';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip';

export default function CardAction() {

    const actions = [
        {
            "text": "Don't get into the car",
            "tooltip": "Ajuda"
        },
        {
            "text": "Get into the car",
            "tooltip": "Ajuda2"
        }
    ]

    return (
        <>
        {actions.map(action => {
            return (
            <Card style={{"marginTop": "20px"}}>
                <Tooltip title={action.tooltip} placement="right" style={{"fontSize": "2em"}}>
                    <Button
                    variant="contained"
                    className="button_action"
                    style={{
                        "backgroundColor": "darkgray",
                        "borderColor": "black",
                        "borderStyle": "double",
                        "borderWidth": "5px",
                        "fontSize": "20px"
                    }}
                    >
                        {action.text}
                    </Button>
                </Tooltip>
            </Card>
            )
        })}
           
        </>
    )
}