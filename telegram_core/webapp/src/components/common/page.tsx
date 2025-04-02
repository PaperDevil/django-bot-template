import React, {PropsWithChildren, useEffect} from "react";
import { hideBackButton, onBackButtonClick, showBackButton } from '@telegram-apps/sdk-react';
import { useNavigate } from 'react-router-dom';


const Page = ({children, back = true}: PropsWithChildren) => {
  const navigate = useNavigate();

  useEffect(() => {
    if (back) {
      showBackButton();
      return onBackButtonClick(() => {
        navigate(-1);
      });
    }
    hideBackButton();
  }, [back]);

  return <>{ children }</>
}

export default Page;