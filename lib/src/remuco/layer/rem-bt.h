#ifndef REMBT_H_
#define REMBT_H_

///////////////////////////////////////////////////////////////////////////////
//
// includes
//
///////////////////////////////////////////////////////////////////////////////

#include <bluetooth/sdp.h>
#include <bluetooth/sdp_lib.h>

#include <remuco/rem-common.h>

///////////////////////////////////////////////////////////////////////////////
//
// types and structs
//
///////////////////////////////////////////////////////////////////////////////

typedef struct {
	guint8	hex[6];
	gchar	str[19];
} rem_bt_addr_t;

typedef struct {
	int		sock;
	rem_bt_addr_t	addr;
} rem_bt_client_t;

typedef struct {
	int		sock;
	sdp_session_t	*sdp_session;
	sdp_record_t	*sdp_record;
} rem_bt_server_t;

///////////////////////////////////////////////////////////////////////////////
//
// functions
//
///////////////////////////////////////////////////////////////////////////////

rem_bt_server_t*
rem_bt_server_up(void);

void
rem_bt_server_down(rem_bt_server_t *srv);

rem_bt_client_t*
rem_bt_client_accept(rem_bt_server_t *srv);

void
rem_bt_client_disconnect(rem_bt_client_t *cli);

#endif /*REMLAYERBT_H_*/
