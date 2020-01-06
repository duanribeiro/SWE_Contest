import React from 'react'
import "./styles.scss"
import Card from '@material-ui/core/Card';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip';

export default function CardAction(props) {

    return (
        <>
        {props.actions.map((action, idx) => {
            return (
            <Card key={`card_${idx}`} style={{"marginTop": "20px"}}>
                <Tooltip
                key={`tooltip_${idx}`}
                title={action.tooltip}
                placement="right"
                style={{"fontSize": "2em"}}
                >
                    <Button
                    key={`button_${idx}`}
                    variant="contained"
                    className="button_action"
                    onClick={() => {
                        props.setStage('')
                        props.fetchStage("introduction_21")
                    }}
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