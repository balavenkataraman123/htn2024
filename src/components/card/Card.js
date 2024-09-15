import "./card.css";

const Card = ({ children, ...rest }) => {
  return <div className="card" {...rest}>{children}</div>;
};

export default Card;
